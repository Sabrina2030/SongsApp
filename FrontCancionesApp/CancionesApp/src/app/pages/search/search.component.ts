import { Component, OnInit } from '@angular/core';
import { MusicserviceService } from '../../services/musicservice.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})

export class SearchComponent implements OnInit {

  
  datos:any = [];
  bandName:string = '';
  constructor (private musicService: MusicserviceService) { }

  ngOnInit(): void {
    
  }

  search(){
    this.musicService.getMusic(this.bandName).subscribe((response) => {
      this.datos = response['canciones'];
      console.log(this.datos);
    });
  }


  mostrar(){
    alert("Estas buscando a: " + this.bandName);
  }
}
