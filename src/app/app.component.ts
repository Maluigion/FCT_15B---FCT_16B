import { Component } from '@angular/core';
import { Post } from './Post';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  posts:Post[] = [
    {
      title: "mon premier post !",
      content: 'youhouuuuuu',
      loveIts: 10,
      created_at: new Date()
    },
    {
      title: "mon deuxième post !",
      content: 'hehehehehehe',
      loveIts: 36,
      created_at: new Date()
    },
    {
      title: "mon dernier post !",
      content: 'snif',
      loveIts: 1,
      created_at: new Date()
    }
  ]

  title = 'blog-openclassroom-angular';
}
