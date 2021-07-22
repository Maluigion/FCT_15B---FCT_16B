import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-post-list-item',
  templateUrl: './post-list-item.component.html',
  styleUrls: ['./post-list-item.component.scss']
})
export class PostListItemComponent implements OnInit {

  @Input() itemTitle!: string;
  @Input() itemContent!: string;
  @Input() itemLikes!: number;
  @Input() itemDate!: any;

  constructor() { }

  ngOnInit(): void {
  }

  onLike() {
    this.itemLikes +=1;
  }

  onDislike() {
    this.itemLikes -=1;
  }

}
