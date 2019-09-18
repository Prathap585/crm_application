import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RestService } from '../_services/rest.service';
import { HttpErrorResponse } from '@angular/common/http';

const URL = 'http://localhost:5000/readxlsx';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  public form: FormGroup;

  constructor(public restService:RestService, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      file: ['']
    });
  }

  onFileChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('file').setValue(file);
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.form.get('file').value);
    this.uploadFile(formData)
  }

  uploadFile(file){
    this.restService.upload(URL, file).subscribe((data) => {
      try {
        console.log(data)
      } catch (error) {
        console.log('Error parsing data for barcode', error);
      }
    }, (err: HttpErrorResponse) => {
      console.log('err wh', err);
    });
  }
}