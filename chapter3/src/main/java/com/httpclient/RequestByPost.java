package com.httpclient;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;

public class RequestByPost {

    public static void main(String[] args) {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        // 无参数Post请求
        /*
        String url = "http://127.0.0.1:8888/post";
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost(url);
        try {
            CloseableHttpResponse httpResponse = httpClient.execute(httpPost);
            System.out.println("**************" + EntityUtils.toString(httpResponse.getEntity()));
        } catch (IOException e) {
            e.printStackTrace();
        }*/

        //有参数Post请求
        String uri = "http://127.0.0.1:8888/post/param";
        HttpPost httpPost = new HttpPost(uri);
        try {
            // 创建参数对象
            ArrayList<BasicNameValuePair> arrayList = new ArrayList<BasicNameValuePair>();
            arrayList.add(new BasicNameValuePair("username", "13668200771"));
            arrayList.add(new BasicNameValuePair("password", "admin123456"));
            UrlEncodedFormEntity urlEncodedFormEntity = new UrlEncodedFormEntity(arrayList, "UTF-8");
            // post请求设置参数
            httpPost.setEntity(urlEncodedFormEntity);
            // post请求设置请求头
            httpPost.setHeader("Content-Type", "application/json;charset=UTF-8");
            httpPost.setHeader("User-Agent",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36");
            // 执行post请求
            CloseableHttpResponse httpResponse = httpClient.execute(httpPost);
            System.out.println(EntityUtils.toString(httpResponse.getEntity()));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (ClientProtocolException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            try {
                httpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
