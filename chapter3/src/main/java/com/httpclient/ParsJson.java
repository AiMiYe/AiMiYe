package com.httpclient;

import com.alibaba.fastjson.JSONObject;
import com.jayway.jsonpath.JsonPath;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class ParsJson {
    public static void main(String[] args) {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse httpResponse=null;
        HttpPost httpPost = new HttpPost("http://127.0.0.1:8888/post");
        String content = null;
        try {
            // 创建JSONObject对象
            JSONObject jsonObject = new JSONObject();
            // 添加参数
            jsonObject.put("username","admin");
            jsonObject.put("password","admin123456");
            // 编码参数
            StringEntity params = new StringEntity(jsonObject.toJSONString(),"UTF8");
            // 设置参数
            httpPost.setEntity(params);
            httpPost.setHeader("Content-Type","application/json");
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
        // json数据解析方式一
        /*
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
         */
        // json数据解析方式二
        // 注意: 1. JsonPath的返回值会自动按照需求的类型进行强转
        //      2. 多节点取值返回的结果是一个数组
        String code = JsonPath.read(content, "$.code");
        System.out.println(code);
        ArrayList<String> message = JsonPath.read(content, "$..message");
        System.out.println(message.get(0));
        HashMap<String, String> map = JsonPath.read(content,"$.content");
        System.out.println(map.get("message"));
        System.out.println(map.get("token"));
    }
}
