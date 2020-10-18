package com.httpclient;

import org.apache.http.Header;
import org.apache.http.HttpResponse;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.Arrays;
import java.util.Locale;
import java.util.ResourceBundle;

public class HttpClientTest {
    private String host;
    private String uri;

    @Test
    public void sendGetRequest() {
        // 初始化get请求对象
        HttpGet httpGet = new HttpGet(this.host + this.uri);
        // 初始化默认请求发送对象
        CloseableHttpClient defaultHttpClient = HttpClients.createDefault();
        // 设置请求配置参数
        RequestConfig config = RequestConfig.custom()
                .setConnectTimeout(1000) // 设置创建链接超时时间
                .setConnectionRequestTimeout(500) // 设置请求超时时间
                .setSocketTimeout(10000) // 设置数据传输的超时时间
                .build();
        httpGet.setConfig(config);
        httpGet.setHeader("User-Agent",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36");
        HttpResponse execute = null;
        try {
            // 发送get请求
            execute = defaultHttpClient.execute(httpGet);
            // 获取响应内容
            String content = EntityUtils.toString(execute.getEntity(),"UTF8");
            System.out.println("响应内容: " + content);
            // 获取响应状态码
            int code = execute.getStatusLine().getStatusCode();
            System.out.println("响应状态码: " + code);
            execute.getLocale().getDisplayLanguage();
            // 获取全部响应头
            Header[] allHeaders = execute.getAllHeaders();
            System.out.println("全部响应头信息: " + Arrays.toString(allHeaders));
            // 获取指定响应头
            Header[] headers = execute.getHeaders("Set-Cookie");
            System.out.println("响应头信息: " + Arrays.toString(headers));
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                defaultHttpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    @BeforeMethod
    public void readConfigurationFile() {
        ResourceBundle resourceBundle = ResourceBundle.getBundle("config", Locale.CHINA);
        this.host = resourceBundle.getString("testHost");
        this.uri = resourceBundle.getString("loginURL");
    }
}
