package com.httpclient;

import org.apache.http.Header;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.cookie.Cookie;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;

public class HttpClientTest {
    private String host;
    private String uri;

    @Test
    public void getCookies(){
        // 创建cookie对象
        BasicCookieStore cookieStore = new BasicCookieStore();
        // 初始化默认请求发送对象并绑定cookie对象
        CloseableHttpClient httpClient = HttpClients.custom().setDefaultCookieStore(cookieStore).build();
        // 初始化get请求对象
        HttpGet httpGet = new HttpGet(this.host + this.uri);

        try {
            // 发送get请求
            HttpResponse execute = httpClient.execute(httpGet);
            // 获取响应内容
            String content = EntityUtils.toString(execute.getEntity());
            System.out.println("响应内容: " + content);
            // 获取cookies
            List<Cookie> cookies = cookieStore.getCookies();
            System.out.println("Cookies: " + Arrays.toString(new List[]{cookies}));
            /*
            for (Cookie cookie: cookies){
                System.out.println("cookieName: "+cookie.getName());
                System.out.println("cookieValue: "+cookie.getValue());
                System.out.println("cookieDomain: "+cookie.getDomain());
                System.out.println("cookiePath: "+cookie.getPath());
                System.out.println("cookieExpiryDate: "+cookie.getExpiryDate());
            }

             */


        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                httpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }
    @Test
    public void sendGetRequest() {
        // 初始化get请求对象
        HttpGet httpGet = new HttpGet(this.host + this.uri);
        // 初始化默认请求发送对象
        CloseableHttpClient defaultHttpClient = HttpClients.createDefault();
        HttpResponse execute = null;
        try {
            // 发送get请求
            execute = defaultHttpClient.execute(httpGet);
            // 获取响应内容
            String content = EntityUtils.toString(execute.getEntity());
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
