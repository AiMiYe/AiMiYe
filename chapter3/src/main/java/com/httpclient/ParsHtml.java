package com.httpclient;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class ParsHtml {
    public static void main(String[] args) {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse httpResponse = null;
        String html = null;
        HttpGet httpGet = new HttpGet("https://www.baidu.com");
        httpGet.setHeader("User-Agent",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36");
        try {
            httpResponse = httpClient.execute(httpGet);
            html = EntityUtils.toString(httpResponse.getEntity(),"utf-8");

        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            try {
                httpClient.close();
                httpResponse.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        System.out.println(html);

    }
}
