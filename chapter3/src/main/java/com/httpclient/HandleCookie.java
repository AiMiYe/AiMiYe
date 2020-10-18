package com.httpclient;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.cookie.Cookie;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.List;

public class HandleCookie {
    private BasicCookieStore cookieStore = null;

    @Test(dependsOnMethods = {"getCookies"})
    public void getUser() {
        // 设置cookie信息
        CloseableHttpClient httpClient = HttpClients.custom().setDefaultCookieStore(cookieStore).build();
        HttpGet get = new HttpGet("http://127.0.0.1:8888/getUser");
        CloseableHttpResponse httpResponse = null;
        try {
            httpResponse = httpClient.execute(get);
            // 获取响应内容
            String data = EntityUtils.toString(httpResponse.getEntity());
            System.out.println("响应内容: " + data);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                httpResponse.close();
                httpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    @Test
    public void getCookies() {
        // 创建cookie对象
        cookieStore = new BasicCookieStore();
        // 初始化默认请求发送对象并绑定cookie对象
        CloseableHttpClient httpClient = HttpClients.custom().setDefaultCookieStore(cookieStore).build();
        // 初始化get请求对象
        HttpGet httpGet = new HttpGet("http://127.0.0.1:8888/login");
        HttpResponse execute = null;
        try {
            // 发送get请求
            execute = httpClient.execute(httpGet);
            // 获取响应内容
            String content = EntityUtils.toString(execute.getEntity(),"UTF8");
            System.out.println("响应内容: " + content);
            // 获取cookies
            List<Cookie> cookies = cookieStore.getCookies();
            System.out.println("Cookies: " + this.cookieStore.toString());
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

}
