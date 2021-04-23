## TestNG测试框架学习记录

## Maven项目引入TestNG包

1. 官方网站下载TestNG包: https://mvnrepository.com/artifact/org.testng/testng

2. IDEA引入TestNG包

3. pom.xml配置文件新增

   ```xml
   <dependencies>
       <!-- https://mvnrepository.com/artifact/org.testng/testng -->
       <dependency>
           <groupId>org.testng</groupId>
           <artifactId>testng</artifactId>
           <version>7.0.0</version>
           <scope>test</scope>
       </dependency>
   </dependencies>
   ```

### TestNG基础注解讲解

1. **@Test**: 该注解表示所修饰方法是: 最基础测试方法
2. **@Ignore**: 该注解表示: 所修饰的方法是一个不会被执行(忽略)的测试用例
3. **@Test(enabled = false)**: 该注解表示: 所修饰的方法是一个不会被执行(忽略)的测试用例
4. **@BeforeMethod**: 该注解表示所修饰的方法是: 每一个 **测试用例(测试方法)** 执行 **之前** 都会执行的方法
5. **@AfterMethod**: 该注解表示所修饰的方法是: 每一个 **测试用例(测试方法)** 执行 **之后** 都会执行的方法
6. **@BeforeClass**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之前** 都会执行的方法
7. **@AfterClass**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之后** 都会执行的方法
8. **@BeforeSuite**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之前** 都会执行的方法 注意: BeforeSuite的执行要**早于**BeforeClass
9. **@AfterSuite**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之后** 都会执行的方法 注意: AfterSuite的执行要**晚于**AfterClass
10. **@BeforeTest**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之前** 都会执行的方法 注意: BeforeTest的执行要**早于** BeforeClass, **晚于** BeforeSuite
11. **@AfterTest**: 该注解表示所修饰的方法是: 每一个 **测试类** 执行 **之后** 都会执行的方法 注意: AfterTest的执行要**晚于**AfterClass, **早于**AfterSuite
12. **@Test(groups = "server")**: 该注解表示对测试用例进行分组, 需要指定组名
13. **@BeforeGroups(groups = "server")**: 该注解表示该组测试用例执行**之前**的方法
14. **@AfterGroups(groups = "server")**: 该注解表示该组测试用例执行**之后**的方法
15. **@Test(expectedExceptions = NullPointerException.class)**: 该注解表示该测试用例执行**之后**存在**预期的异常**
16. **@Test(dependsOnMethods ={ "testCase1", "testCase3"})**: 该注解表示:运行修饰的测试用例时会先执行依赖的测试用例, 如果依赖的测试**都**执行成功, 则会执行修饰的测试用例. 否则忽略修饰的测试用例; 如果所依赖的多个测试用例,依赖的测试用例之间相互独立互不不影响
17. **@Test(invocationCount = 15, threadPoolSize = 5)**: 该注解表示使用多线程执行该测试用例. 注意: 需要指定线程数大小以及线程池大小
18. **@Test(timeOut = 3000)**:  该注解表示超时测试用例, 时间单位毫秒. 超过超时时间, 测试用例判定失败

### Moco基本使用

1. 启动命令

   java -jar ./moco-12.jar 协议 -p 端口号 -c json配置文件
   
2. json文件解析:

   1. **"description"**: 添加注释信息, 请求是不会返回
   2. **"request"**: 设置请求信息
      1. **"uri"**: 设置请求路径
      2. **"method"**: 设置请求方式
      3. **"queries"**: 设置**get**请求参数, 内容为一个字典
      4. **"forms"**: 设置**post**请求参数, 表单格式
      5. **"cookies"**: 设置请求携带cookie信息
      6. **"json"**: 设置请求参数为json格式数据
      7. **"headers"**: 设置请求头信息
   3. **"response"**: 设置返回信息
      1. **"text"**: 设置返回文本信息
      2. **"status"**: 设置返回状态码
      3. **"json"**: 设置响应参数为json格式数据
      4. **"headers"**: 设置响应头信息
      5. **"file"**: 设置返回文件
   4. **"redirectTo"**: 设置重定向

### HTTP常用头字段

1. 请求头
   1. **Accept**: 表示客户端告诉服务器它所支持的数据类型
   2. **Accept-Charset**: 表示客户端告诉服务器它所支持的字符集
   3. **Accept-Encoding**: 表示客户端告诉服务器它所支持的数据压缩格式
   4. **Accept-Language**: 表示客户端告诉服务器它所使用的语言
   5. **Host**: 表示客户端告诉服务器它所访问的域名
   6. **If-Modified-Since**: 表示客户端告诉服务器它缓存数据有效时间
   7. **Referer**: 表示客户端告诉服务器它的请求来源域名
   8. **User-Agent**: 表示客户端告诉服务器它的浏览器类型,版本等信息
   9. **Date**: 表示客户端告诉服务器访问时间
   10. **Connection**: 表示客户端告诉服务器它的链接方式
       1. keep-alive: 表示长链接
       2. close: 表示短连接
   11. **Content-Type**: 表示客户端告诉服务器请求数据类型
2. 响应头
   1. **Location**: 表示服务器告诉客户端重定向域名
   2. **Server**: 表示服务器告诉客户端服务器的类型
   3. **Content-Encoding**: 表示服务器告诉客户端响应数据压缩格式
   4. **Content-Type**: 表示服务器告诉客户端响应数据类型
   5. **Last-Modified**: 表示服务器告诉客户端数据最后修改时间
   6. **Refresh**: 表示用于控制浏览器定时刷新


