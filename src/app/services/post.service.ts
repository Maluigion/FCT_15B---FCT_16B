import { Injectable } from '@angular/core';
import { Post } from '../models/Post.model';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostService {

  postsSubject = new Subject<Post[]>();

  private posts:Post[] = [
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

  emitPostSubject() {
    this.postsSubject.next(this.posts.slice());
  }

  addPost(post: Post) {
    this.posts.push(post);
    this.emitPostSubject();
  }

  removePost(index: number) {
    this.posts.splice(index,1);
  }

  LikePost(index: number) {
    this.posts[index].loveIts +=1;
  }

  DislikePost(index: number) {
    this.posts[index].loveIts -=1;
  }

  constructor() { }
}
