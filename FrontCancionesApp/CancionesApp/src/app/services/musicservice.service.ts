import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})

export class MusicserviceService {

  url = 'http://127.0.0.1:4000/search_tracks?name=';
  constructor(private http: HttpClient) { }

  getMusic(bandName: string): Observable<any> {
    return this.http.get(this.url + bandName);
  }
}
