import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NewPostComponent } from './components/new-post/new-post.component';
import { AppComponent } from './app.component';
import { PostViewComponent } from './components/post-view/post-view.component';

const routes: Routes = [
  { path: 'posts', component: PostViewComponent },
  { path: 'new', component: NewPostComponent },
  { path: '**', redirectTo: 'posts' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
