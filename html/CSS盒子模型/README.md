# CSS盒子模型

CSS三大特性：
1. [继承性](https://www.bilibili.com/video/BV1Kg411T7t9?p=83)
2. [层叠行](https://www.bilibili.com/video/BV1Kg411T7t9?p=84)
3. 优先级，看p88然后再[做题](https://www.bilibili.com/video/BV1Kg411T7t9?p=89)


[Chrome调试](https://www.bilibili.com/video/BV1Kg411T7t9?p=90)！！！

[综合案例——新浪导航](https://www.bilibili.com/video/BV1Kg411T7t9?p=98)，见p98！！！

[综合案例——新闻列表](https://www.bilibili.com/video/BV1Kg411T7t9?p=107)，见p107！！！


### p87_优先级测试：当一个标签使用了多个选择器，样式冲突的时候，到底谁生效
- 优先级公式（选择范围越广，优先级越低）：`继承 < 通配符选择器 < 标签选择器 < 类选择器 < id选择器 < 行内样式 < !important`
- `!important`写在属性值的后面，分号的前面
- `!important`不能提升继承的优先级，**只要是继承优先级最低**！
- 实际开发中不建议使用`!important`

### p88_优先级叠加计算：
- 如果是复合选择器，此时需要通过权重叠加计算方法，判断最终哪个选择器优先级最高会生效
- 权重叠加计算公式（每一级之间不存在进位）：`(0,0,0,0)`。代表的是复合选择器中`(行内样式的个数,id选择器的个数,类选择器的个数,标签选择器的个数)`
- 比较规则：
    - 先比较第一级数字，如果比较出来了，之后的统统不看
    - 如果第一级数字相同，再去比较第二级数字，如果比较出来了，之后的统统不看
    - 以此类推
    - 如果最终所有数字都相同，表示优先级相同，则比较重叠性（谁写在下面，谁说了算）
- 注意：`!important`如果不是继承，则权重最高！
### p94_盒子模型组成：
- CSS中规定每个盒子分别由：内容区域（content）、内边距区域（padding）、边框区域（border）、外边距区域（margin）构成，这就是盒子模型。
- 内容的宽度和高度
    - 作用：利用width和height属性默认设置**盒子内容**区域的大小
    - 属性：`width/height`
    - 常见取值：`数字+px`
- 边框`border`
    - 全部边框，属性名：`border`
    - 单方向边框，属性名：`border-方位名词`
    - 属性值：单个取值的连写，取值之间以空格隔开，没有顺序要求，如`border: 10px soild red`，（粗细、线条样式、颜色）
    - `soild`：实线；`dashed`：虚线；`dotted`：点线
    - 快捷键：`bd+tab`
    - **边框线会撑大盒子的**，`最终盒子的尺寸=内容的width/height+边框线`
- 内边距`padding`
    - `padding`属性，`padding: 20px;`表示四个边距都是20px
    - `padding`属性也可以当作复合属性使用，表示单独设置某个方向的内边距。（从上开始顺时针，如果数不够就取跟对面相同的值）
    - `padding: 10px 20px 40px 80px;`（上、右、下、左）
    - `padding: 10px 40px 80px;`（上、左右、下）
    - `padding: 10px 80px;`（上下、左右）
    - **内边距也会撑大盒子**！
- 外边距`margin`
    - 与内边距写法一样。外边距有一些[问题](https://www.bilibili.com/video/BV1Kg411T7t9?p=110)。
    - 外边距问题1（合并）：垂直布局的块级元素，上下的margin会合并，最终两者的距离为margin的最大值。解决办法：只给其中一个盒子设置`margin`即可。
    - 外边距问题2（坍塌）：互相嵌套的块级元素，子元素的`margin-top`会作用在父元素上，导致父元素一起往下移动。解决办法：
        - 给父元素设置`border-top`或者`padding-top`（分割父子元素的`margin-top`）
        - 给父元素设置`overflow: hidden`
        - 转换成行内块元素
        - 设置浮动
- 其他
    - 边框跟内边距都会撑大盒子，导致在设计的时候，要自己计算内容的宽高。可以采用两种方法解决，一种是手动内减。另一种是自动内减，给盒子设置属性（`box-sizing:border-box`）即可，浏览器会自动计算多余大小，自动在内容中减去。（只有CSS3可以）
### p105_清除默认样式：
- 浏览器默认会给部分标签设置默认的margin和padding，但一般在项目开始之前需要先清除这些标签默认的margin和padding，后续自己设置。
- 比如`body`有默认`margin: 8px`；`p`有默认上下的`margin`；`ul`有默认的上下`margin`和`padding-left`。
- 清除方法：`* {margin: 0; padding: 0;}`
### p106_版心居中：
- 版心：网页的有效内容。居中就是加个外边距就可以啦。
- `margin: 0 auto;`，上下是0，左右是自动居中
### p111_行内元素的内外边距问题：
- 如果想要通过`margin`或`padding`改变行内标签的垂直位置的，无法生效。也就是说：
- 行内标签的`margin-top`和`margin-bottom`不生效
- 行内标签的`padding-top`和`padding-bottom`不生效
- 要么转显示模式，要么就通过行高改