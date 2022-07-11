<?php

namespace App\Http\Controllers\Frontend;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Course;
use App\Models\TeacherInfo;
use App\Models\StudentInfo;
use Illuminate\Support\Str;
use App\Models\Dept;
use Carbon\Carbon;
use Image;
class CourseController extends Controller
{


    public function InfoView(){
        $infos = Course::latest()->get();
        $depts = Dept::orderBy('dept','ASC')->get();
        return view('frontend.student_info.add_course',compact('infos','depts'));
    }

    public function InfoStore(Request $request){
        $request->validate([

            'dept_id'=>'required',
            'batch'=>'required',
            'course_no'=>'required',
            'course_name'=>'required',
        ],
        [

            'dept_id.required'=>'Select Department Name',
            'batch.required'=>'Select Batch NO',
            'course_no.required'=>'Insert Course No',
            'course_name.required'=>'Insert Course Name',
        ]);




        Course::insert([

            'dept_id'=>$request->dept_id,
            'batch'=>$request->batch,
            'course_no'=>$request->course_no,
            'course_name'=>$request->course_name,
            'created_at'=>Carbon::now(),
        ]);
        $notification = array(
            'message'=>'Course Info Inserted Successfully',
            'alert-type'=>'success'
        );
        return redirect()->back()->with($notification);
    }

}


