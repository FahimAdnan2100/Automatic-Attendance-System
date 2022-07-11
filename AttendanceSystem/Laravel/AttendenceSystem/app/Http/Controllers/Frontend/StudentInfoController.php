<?php

namespace App\Http\Controllers\Frontend;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\TeacherInfo;
use App\Models\StudentInfo;
use Illuminate\Support\Str;
use App\Models\Dept;
use Carbon\Carbon;
use Image;
class StudentInfoController extends Controller
{
    public function InfoView(){
        $infos = StudentInfo::latest()->get();
        $depts = Dept::orderBy('dept','ASC')->get();
        return view('frontend.student_info.student_info_add',compact('infos','depts'));
    }

    public function InfoStore(Request $request){
        $request->validate([
            'name'=>'required',
            's_id'=>'required',
            'dept_id'=>'required',
            'batch'=>'required',
            'email'=>'required',
            'phone'=>'required',
            'student_photo_path'=>'required',



        ],
        [
            'name.required'=>'Insert Student Name',
            's_id.required'=>'Insert Student ID',
            'dept_id.required'=>'Select Department Name',
            'batch.required'=>'Select Batch No',
            'email.required'=>'Insert Student Email',
            'phone.required'=>'Insert Student Phone Number',
            'student_photo_path.required'=>'Select Teacher Image',
        ]);

        $dept_name = $request->dept_id;
        $depts = Dept::latest()->get();
        foreach($depts as $dep){
            if($dept_name == $dep->id){
                $dept_n=$dep->dept;
            }
        }
        $name = $request->name;
        $batch = $request->batch;
        $image = $request->file('student_photo_path');
        $name_gen = $name.'.'.$image->getClientOriginalExtension();
        $d=Str::slug(strtoupper($dept_n));
        $dirPath = public_path('upload/student_images/'.$d.'/'.$batch);
            if (!file_exists($dirPath)) {
                mkdir($dirPath, 0777, true);
                }
        Image::make($image)->save('upload/student_images/'.$dept_n.'/'.$batch.'/'.$name_gen);
        $save_url='upload/student_images/'.$dept_n.'/'.$batch.'/'.$name_gen;


        StudentInfo::insert([
            'name'=>$request->name,
            's_id'=>$request->s_id,
            'dept_id'=>$request->dept_id,
            'batch'=>$request->batch,
            'email'=>$request->email,
            'phone'=>$request->phone,
            'student_photo_path'=>$save_url,
            'created_at'=>Carbon::now(),
        ]);
        $notification = array(
            'message'=>'Student Info Inserted Successfully',
            'alert-type'=>'success'
        );
        return redirect()->back()->with($notification);
    }

}
