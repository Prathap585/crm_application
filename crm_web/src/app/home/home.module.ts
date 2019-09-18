import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HomeRoutingModule } from './home.routes'
import { HomeComponent } from './home.component'
import { AngularMaterialModule } from '../angular-material.module'

@NgModule({
    imports:[
        CommonModule,
        HomeRoutingModule,
        AngularMaterialModule,
        FormsModule,
        ReactiveFormsModule
    ],
    declarations:[
        HomeComponent
    ],
    exports:[
        HomeComponent
    ],
    providers:[]
})
export class HomeModule{

}