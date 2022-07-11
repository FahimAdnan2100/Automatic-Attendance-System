<?php

namespace App\Http\Controllers\Frontend;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Storage;
use Illuminate\Http\Request;
use App\Models\TeacherInfo;
use Illuminate\Support\Str;
use App\Models\Dept;
use Carbon\Carbon;
use Image;
class TeacherInfoController extends Controller
{
    public function InfoView(){
        $infos = TeacherInfo::latest()->get();
        $depts = Dept::orderBy('dept','ASC')->get();
        return view('frontend.student_info.add_info',compact('infos','depts'));
    }

    public function InfoStore(Request $request){
        $request->validate([
            'name'=>'required',
            'dept_id'=>'required',
            'teacher_photo_path'=>'required',
        ],
        [
            'name.required'=>'Insert Teacher Name',
            'dept_id.required'=>'Select Department Name',
            'teacher_photo_path.required'=>'Select Teacher Image',
        ]);

        $dept_name = $request->dept_id;
        $depts = Dept::latest()->get();
        foreach($depts as $dep){
            if($dept_name == $dep->id){
                $dept_n=$dep->dept;
            }
        }
        $name = $request->name;
        $image = $request->file('teacher_photo_path');
        $name_gen = $name.'.'.$image->getClientOriginalExtension();
        $dirPath = public_path('upload/teacher_images/' . Str::slug(strtoupper($dept_n),'-'));
            if (!file_exists($dirPath)) {
                mkdir($dirPath, 0777, true);
                }
        Image::make($image)->save('upload/teacher_images/'.$dept_n.'/'.$name_gen);
        $save_url='upload/teacher_images/'.$dept_n.'/'.$name_gen;


        TeacherInfo::insert([
            'name'=>$request->name,
            'dept_id'=>$request->dept_id,
            'teacher_photo_path'=>$save_url,
            'created_at'=>Carbon::now(),
        ]);
        $notification = array(
            'message'=>'Teacher Info Inserted Successfully',
            'alert-type'=>'success'
        );
        return redirect()->back()->with($notification);
    }

}
