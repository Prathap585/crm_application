import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) { }

  get(url) {
    var reqHeader = new HttpHeaders({
      'Content-Type': 'application/json',
    });
    return this.http.get<any>(url)
  }

  upload(url, file) {
    var reqHeader = new HttpHeaders({
      'Content-Type': 'multipart/form-data',
    });
    return this.http.post<any>(url, file);
  }

  patch(url, shippingRecord) {
    var reqHeader = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Request-Method': '*',
    });
    return this.http.patch<any>(url, shippingRecord, { headers: reqHeader });
  }

}
