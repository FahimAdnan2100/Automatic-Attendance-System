<?php

namespace App\Http\Controllers\Frontend;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\TeacherInfo;
use App\Models\StudentInfo;
use App\Models\StudentAttendance;
use Illuminate\Support\Str;
use App\Models\Dept;
use App\Models\Course;
use Carbon\Carbon;
use Image;

class InfoController extends Controller
{
    public function BatchView(Request $request,$depts){
        #$dept=$request->$depts;

        return view('frontend.student_info.batch',compact('depts'));

    }

    public function CourseView(Request $request,$batch,$deptt){
        $depts = Dept::all();
        foreach($depts as $d){
            if($deptt==$d->id){
                $dd=$d->dept;

            }
        }
        #dd($dd);
        #$years = StudentAttendance::where('dept',$dd)->where('batch',$batch)->get();
        $courses = Course::where('dept_id',$deptt)->where('batch',$batch)->get();
        return view('frontend.student_info.course',compact('batch','dd','courses'));
    }

    public function InfoYear(Request $request,$course_no,$batch,$dept){
        #$years = StudentAttendance::where('dept',$dept)->where('batch',$batch)->where('course_no',$course_no)->get();
        return view('frontend.student_info.year',compact('batch','course_no','dept'));
    }

    public function InfoMonth(Request $request,$year,$course_no,$batch,$dept){
        #$months = StudentAttendance::where('dept',$dept)->where('batch',$batch)->where('course_no',$course_no)->where('year',$year)->get();
        return view('frontend.student_info.month',compact('year','batch','course_no','dept'));
    }
    public function InfoDay(Request $request,$month,$year,$course_no,$batch,$dept){
        #$days = StudentAttendance::where('dept',$dept)->where('batch',$batch)->where('course_no',$course_no)->where('year',$year)->where('month',$month)->get();
        return view('frontend.student_info.day',compact('month','year','batch','course_no','dept'));
    }
    public function AttendanceInfo(Request $request,$date,$month,$year,$course_no,$batch,$dept){
        if($month=='1'){
            $month='January';
        }
        elseif($month=='2'){
            $month='February';
        }
        elseif($month=='3'){
            $month='March';
        }
        elseif($month=='4'){
            $month='April';
        }
        elseif($month=='5'){
            $month='May';
        }
        elseif($month=='6'){
            $month='June';
        }
        elseif($month=='7'){
            $month='July';
        }
        elseif($month=='8'){
            $month='August';
        }
        elseif($month=='9'){
            $month='September';
        }
        elseif($month=='10'){
            $month='October';
        }
        elseif($month=='1'){
            $month='November';
        }
        elseif($month=='12'){
            $month='December';
        }
        if($date=='1' || $date=='2' || $date=='3' || $date=='4' || $date=='5' || $date=='6' || $date=='7' || $date=='8' || $date=='9' ){
           $date='0'.$date;
           #dd($date);
        }else{
            $date=$date;
        }
        #dd("0".$date);


        #dd($dept,$batch,$course_no,$year,$month,$date);
        #where('dept',$dept)->where('batch',$batch)->where('course_no',$course_no)->where('year',$year)->where('month',($month))->where('date',$date)->get()
        $attendances = StudentAttendance::where('dept',$dept)->where('batch',$batch)->where('course_no',$course_no)->where('year',$year)->where('month',($month))->where('date',($date))->get();

        #
        #dd($attendances);
        return view('frontend.student_info.student_attendance',compact('attendances'));
    }
}
