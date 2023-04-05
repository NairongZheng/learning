# ddp 分布式训练
[参考链接](https://www.bilibili.com/video/BV1eD4y1F7o4)


## DDP单机多卡
- 初始化进程组：`torch.distributed.init_process_group('nccl', world_size=n_gpus, rank=args.local_rank)`
    - 'nccl'：GPU之间的通信方式，有多种方法
    - world_size：当前这个节点上(机子)有多少个GPU卡（如果是多机的话，每个机子都要运行这个代码，都要分别指定这台机子多少个GPU）
    - rank：当前进程在哪个GPU卡上，args.local_rank是通过外部的torch.distributed.launch传入的
- 指定当前进程所能用到的GPU卡的名称：`torch.cuda.set_device(args.local_rank)`
    - 这个相当于`os.environ["CUDA_VISIBLE_DEVICE"] = "0"`这个环境变量的设置
- 对模型进行包裹
    - `model = DistributedDataParallel(model.cuda(args.local_rank), device_ids=[args.local_rank])`
- 对数据进行分配：`train_sampler = DistributedSampler(train_dataset)`
    - 把train_dataset中的数据**随机分配**到不同GPU上
- 生成Dataloader：`train_dataloader = DataLoader(..., sampler=train_sampler)`
    - DataLoader接收了sampler之后就不需要定义shuffle了，因为sampler就是指定了顺序了，再shuffle就没意义了，具体看看sampler的源码
- 数据拷贝：`data = data.cuda(args.local_rank)`
- 执行命令：`python -m torch.distributed.launch --nproc_per_node=n_gpus train.py`
    - `torch.distributed.launch`会构建很多个进程，进程数由每个节点的卡数(nproc_per_node)指定的
- 模型保存与加载：
    - `torch.save`在`local_rank=0`的位置进行保存，同样注意调用`model.module.state_dict()`
    - `torch.load`注意map_location
- 注意事项：
    - train.py中要有接收local_rank的参数选项，launch会传入这个参数
    - 每个进程的batch_size应该是一个GPU所需要的batch_size大小，与DataParallel不一样！
    - 在每个周期开始处，调用`train.sampler.set_epoch(epoch)`可以使得数据充分打乱
    - 有了sampler就不要在DataLoader中设置shuffle=True了


## DDP多机多卡
- 代码编写流程与单机多卡一致
- 执行命令（以两个节点为例，每个节点处有n_gpus个GPU）
    - `python -m torch.distributed.launch --nproc_per_node=n_gpus --nnodes=2 --node_rank=0 --master_addr='主节点IP' --master_port='主节点端口' train.py`
    - `python -m torch.distributed.launch --nproc_per_node=n_gpus --nnodes=2 --node_rank=1 --master_addr='主节点IP' --master_port='主节点端口' train.py`
    - 只有在每个节点都运行了命令之后，代码才会开始跑
- 模型保存与加载与单机多卡一致