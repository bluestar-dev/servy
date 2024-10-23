import { Component, OnInit } from '@angular/core';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  template: `
    <h1>Multi-Service App</h1>
    <h2>Food Items</h2>
    <ul>
      <li *ngFor="let item of foodItems">{{ item.name }} - {{ item.price }}</li>
    </ul>
  `
})
export class AppComponent implements OnInit {
  foodItems: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.getFoodItems().subscribe(data => this.foodItems = data);
  }
}
