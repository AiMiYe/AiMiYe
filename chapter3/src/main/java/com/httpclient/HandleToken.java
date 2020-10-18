package com.httpclient;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.impl.cookie.BasicClientCookie;
import org.apache.http.util.EntityUtils;
import org.testng.annotations.Test;

import java.io.IOException;

public class HandleToken {
    private String token = null;

    @Test(dependsOnMethods = {"getToken"})
    public void postUser() {
        // 创建cookie对象
        BasicClientCookie token = new BasicClientCookie("token", this.token);
        // 设置cookie属性
        token.setPath("/");
        token.setDomain("127.0.0.1");
        token.setExpiryDate(null);
        System.out.println(token);

        // 创建cookieStore对象
        BasicCookieStore store = new BasicCookieStore();
        // 将cookie对象绑定到cookieStore对象中
        store.addCookie(token);
        // 将cookieStore对象绑定到httpClient对象中
        CloseableHttpClient httpClient = HttpClients.custom().setDefaultCookieStore(store).build();
        HttpGet httpGet = new HttpGet("http://127.0.0.1:8888/postUser");
        CloseableHttpResponse httpResponse = null;
        try {
            httpResponse = httpClient.execute(httpGet);
            System.out.println("状态码: " + httpResponse.getStatusLine().getStatusCode());
            System.out.println("响应内容: " + EntityUtils.toString(httpResponse.getEntity()));
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            try {
                httpResponse.close();
                httpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    @Test
    public void getToken() {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse httpResponse = null;
        HttpPost httpPost = new HttpPost("http://127.0.0.1:8888/post");
        String content = null;
        try {
            // 创建Json对象
            JSONObject jsonObject = new JSONObject();
            //设置参数
            jsonObject.put("username","admin");
            jsonObject.put("password","admin123456");
            System.out.println(jsonObject.toJSONString());
            // 编码参数数组
            StringEntity params = new StringEntity(jsonObject.toJSONString(), "UTF-8");
            // 设置请求参数
            httpPost.setEntity(params);
            httpPost.setHeader("Content-Type","application/json");
            // 发送请求
            httpResponse = httpClient.execute(httpPost);
            content = EntityUtils.toString(httpResponse.getEntity(), "UTF8");
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
        System.out.println("响应内容: " + content);
        // {"code":"0","content":{"message":"登陆成功","token":"20201012200627"},"list":[1,5,8]}
        // 解析json字符串为json对象
        JSONObject jsonObject = JSON.parseObject(content);
        // 获取json对象的子对象
        JSONObject cont = jsonObject.getJSONObject("content");
        this.token = cont.getString("token");

    }
}
