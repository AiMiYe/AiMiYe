package com.httpclient;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

public class RequestByGet {
    private CloseableHttpResponse httpResponse = null;
    // 创建HttpClient对象
    private final CloseableHttpClient httpClient = HttpClients.createDefault();

    public RequestByGet() {
    }

    public CloseableHttpResponse getHttpResponse() {
        return httpResponse;
    }

    public void getRequest(String uri) {
        // 创建Get请求对象
        HttpGet httpGet = new HttpGet(uri);
        try {
            // HttpClient对象执行Get请求
            this.httpResponse = this.httpClient.execute(httpGet);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void getRequest(String uri, HashMap<String, String> param) {

        try {
            //创建设置get参数对象
            URIBuilder uriBuilder = new URIBuilder(uri);
            // 添加参数
            for (Map.Entry<String, String> entry : param.entrySet()) {
                uriBuilder.addParameter(entry.getKey(), entry.getValue());
            }
            // 创建Get请求对象
            HttpGet httpGet = new HttpGet(uriBuilder.build());
            // HttpClient对象执行Get请求
            httpResponse = httpClient.execute(httpGet);
        } catch (URISyntaxException e) {
            e.printStackTrace();
        } catch (ClientProtocolException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void close() {
        try {
            this.httpResponse.close();
            this.httpClient.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getResponseBody(){
        String content = null;
        try {
            content = EntityUtils.toString(this.httpResponse.getEntity());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content;
    }
    public static void main(String[] args) {
        String param = "http://localhost:8888/login/param";
//        String login = "http://localhost:8888/login";
        HashMap<String, String> map = new HashMap<String, String>();
        map.put("username", "13668200771");
        map.put("password", "admin123456");
        RequestByGet requestByGet = new RequestByGet();
        requestByGet.getRequest(param, map);
//        requestByGet.getRequest(login);
        System.out.println(requestByGet.getResponseBody());
        requestByGet.close();
    }
}
