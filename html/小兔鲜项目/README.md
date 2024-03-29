# 小兔鲜项目搭建

**项目见xtx-px-client**

### p168_CSS精灵图
- 场景：项目中将多张小图片，合并成一张大图片，这张大图片称之为精灵图
- 优点：减少服务器发送次数，减轻服务器的压力，提高页面加载速度
- 例如：需要在网页中展示8张小图片
    - 8张小图片分别发送：发送8次
    - 合成一张精灵图发送：发送1次
- 精灵图的标签都用行内标签：`span, b, i...`

### p169_精灵图使用：
- 创建一个盒子，设置盒子的尺寸和小图尺寸相同
- 将精灵图设置为盒子的背景图片
- 修改背景图的位置：测量小图片左上角坐标，分别**取负值**设置给盒子的`background-position: x y`

### p170_背景图缩放
- 设置背景图片的大小`background-size: 宽度 高度`
    - `数字+px`：简单方便，常用
    - `百分比`：相对于对当前盒子自身的宽高百分比
    - `contain`：包含，将背景图片等比缩放，直到不会超出盒子的最大。导致盒子可能有留白
    - `cover`：覆盖，将背景图片等比缩放，直到刚好填满整个盒子没有空白。导致图片显示不全
    - 工作中, 图的比例和盒子的比例都是相同的, contain 和cover效果完全相同
- 连写：`background: color image repeat position size`
- `background-size`和`background`连写同时设置时，需要注意覆盖问题。可以把单独的样式写在连写的下面。

### p171_盒子阴影
- 给盒子添加阴影效果，吸引用户注意，体现页面的制作细节`box-shadow`
    - `h-shadow`：必须，水平偏移量，允许负值
    - `v-shadow`：必须，垂直偏移量，允许负值
    - `blur`：可选，模糊度
    - `spread`：可选，阴影扩大
    - `color`：可选，阴影颜色
    - `inset`：可选，将阴影改为内部阴影

### p172_过渡
- 让元素的样式慢慢的变化，常配合hover使用，增强网页交互体验`transition`
    - 过渡的属性：
        - `all`：所有能过渡的属性都过渡
        - `具体属性名如width`：只有width过渡
    - 过渡的时长：`数字+s（秒）`
- **过渡配合hover使用, 谁变化谁加过渡属性**
- 过渡需要：默认状态和`hover`状态样式不同，才能有过渡效果
- `transition`属性给需要过渡的元素本身加
- `transition`属性设置在不同状态中，效果不同
    - 给默认状态设置，鼠标移入移出都有过渡效果
    - 给`hover`状态设置，鼠标移入有过渡效果，移出没有过渡效果

### p173_骨架
- `<!DOCTYPE html>`：文档类型声明，告诉浏览器该网页的html版本
- `<html lang="en">`：标识网页使用的语言。
    - 作用：搜索引擎归类+浏览器翻译
    - 常见语言：zh-CN 简体中文 / en 英文
- `<meta charset="UTF-8">`：标识网页使用的字符编码
    - `UTF-8`：万国码，国际化的字符编码，收录了全国语言的文字
    - `GB2312`：6000+ 汉字
    - `GBK`：20000+ 汉字
    - 开发中统一使用`UTF-8`字符编码即可
- `<meta http-equiv="X-UA-Compatible" content="IE=edge">`：ie（兼容性差） / edge
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`：移动端网页的时候要用（宽度=设备宽度）

### p174_SEO
- SEO(Search Engine Optimization)：搜索引擎优化。让网站在搜索引擎上的排名靠前。
    - 提升SEO的常见方法：
        - 竞价排名
        - 将网页制作成html后缀
        - 标签语义化（在合适的地方使用合适的标签）
    - SEO三大标签：
        - `title`：网页标题标签
        - `description`：网页描述标签
        - `keywords`：网页关键词标签
    - 设置图标：`link:favicon`，一般图标放在项目文件夹第一层里

### p176_项目目录
- 新建项目文件夹xtx-pc-client，在VScode种打开
    - 在实际开发中，项目文件夹不建议使用中文
    - 所有项目相关文件都保存在xtx-pc-client目录中
- 复制favicon.ico到xtx-pc-client目录中
    - 一般习惯将ico图标放在项目根目录
- 复制images和uploads目录到xtx-pc-client目录中
    - images：存放网站固定使用的图片素材，如：logo、样式修饰图片
    - uploads：存放网站非固定使用的图片素材，如：商品图片、宣传图片
- 新建index.html在根目录
- 新建css文件夹保存网站的样式，并新建以下CSS文件：
    - base.css：基础公共样式
    - common.css：该网站中多个网页相同的模块的重复样式，如：头部、底部
    - index.css：首页样式