# bs爬虫
[参考视频](https://www.bilibili.com/video/BV1d54y1g7db)

## 状态码
1. 2开头：成功
   1. 200：OK，客户端请求成功
2. 3开头：重定向，需要进一步操作
   1. 301：Moved permanently，资源被永久移动到新地址
3. 4开头：客户端错误，如请求错误或请求资源无效
   1. 400：Bad Request，客户端不能被服务器所理解
   2. 401：Unauthorized，请求未经授权
   3. 403：Forbidden，服务器拒绝提供服务
   4. 404：Not Found，请求资源不存在
4. 5开头：服务器错误，比如出现问题或正在维护
   1. 500：Internal Server Error，服务器发生不可预期的错误
   2. 503：Server Unavailable，服务器当前不能处理客户端的请求


## html常用标签
1. 标题：`<h1></h1>`(h1-h6)
2. 文本段落：`<p></p>`
3. 换行：`<br>`
4. 加粗：`<b></b>`
5. 斜体：`<i></i>`
6. 下划线：`<u></u>`
7. 图片：`<img scr=...>`
8. 链接：`<a href=...>`
9. 容器-块级元素：`<div></div>`
9. 容器-内联元素：`<span></span>`
10. 有序列表：`<ol></ol>`
10. 无序列表：`<ul></ul>`
11. 列表元素：`<li></li>`
12. 表格：`<table></table>`
    1.  表格头部：`<thead></thead>`
    1.  表格主题：`<tbody></tbody>`
    2.  表格行：`<tr></tr>`
    3.  单元格：`<td></td>`