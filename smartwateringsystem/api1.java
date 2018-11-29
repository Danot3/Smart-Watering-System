package com.example.smartwateringsystem;


        import java.util.List;
        import retrofit2.Call;
        import retrofit2.http.GET;

    public interface api1 {
        String BASE_URL  = "http://172.20.10.8:8080/application/";
        @GET("getdata.php")
        Call<List<Hero>> getnum();

    }

