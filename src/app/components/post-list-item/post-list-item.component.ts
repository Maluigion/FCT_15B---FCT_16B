import { Component, OnInit, Input } from '@angular/core';
import { Post } from 'src/app/models/Post.model';
import { PostService } from 'src/app/services/post.service';

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
  @Input() index!: number;

  constructor(private postService: PostService) { }

  ngOnInit(): void {
  }

  onLike(index: number) {
    this.postService.LikePost(index);
    this.postService.emitPostSubject();
  }

  onDislike(index: number) {
    this.postService.DislikePost(index);
    this.postService.emitPostSubject();
  }

  onDelete(index: number) {
    this.postService.removePost(index);
    this.postService.emitPostSubject();
  }

}
