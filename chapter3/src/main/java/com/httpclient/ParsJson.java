package com.httpclient;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.util.ArrayList;

public class ParsJson {
    public static void main(String[] args) {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse httpResponse=null;
        HttpPost httpPost = new HttpPost("http://127.0.0.1:8888/post");
        String content = null;
        try {
            // 创建参数数组
            ArrayList<BasicNameValuePair> arrayList = new ArrayList<BasicNameValuePair>();
            arrayList.add(new BasicNameValuePair("username","admin"));
            arrayList.add(new BasicNameValuePair("password","admin123456"));
            // 编码参数数组
            UrlEncodedFormEntity params = new UrlEncodedFormEntity(arrayList, "UTF8");
            // 设置参数
            httpPost.setEntity(params);
            // 发送请求
            httpResponse = httpClient.execute(httpPost);
            content = EntityUtils.toString(httpResponse.getEntity(),"UTF8");
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
        System.out.println("响应内容: " + content);
        // {"code":"0","content":{"message":"登陆成功","token":"20201012200627"},"list":[1,5,8]}
        // 解析json字符串为json对象
        JSONObject jsonObject = JSON.parseObject(content);
        // 获取指定key的字符串值
        String code = jsonObject.getString("code");
        System.out.println(code);
        // 获取json对象的子对象
        JSONObject cont = jsonObject.getJSONObject("content");
        String token = cont.getString("token");
        System.out.println(token);
        // 获取json数组对象
        JSONArray list = jsonObject.getJSONArray("list");
        System.out.println(list);
        list.forEach(System.out::println);

    }
}
