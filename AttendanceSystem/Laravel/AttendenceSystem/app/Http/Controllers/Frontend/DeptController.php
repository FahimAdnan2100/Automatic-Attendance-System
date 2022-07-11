<?php

namespace App\Http\Controllers\Frontend;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Dept;
use Carbon\Carbon;

class DeptController extends Controller
{
    public function DeptView(){
        $depts = Dept::latest()->get();
        return view('frontend.student_info.add_department',compact('depts'));
    }
    public function DeptStore(Request $request){
        $request->validate([
            'dept'=>'required',
        ],
        [
            'dept.required'=>'Insert Department Name',
        ]);
        Dept::insert([
            'dept'=>strtoupper($request->dept),
            'created_at'=>Carbon::now(),
        ]);
        $notification = array(
            'message'=>'Department Inserted Successfully',
            'alert-type'=>'success'
        );
        return redirect()->back()->with($notification);
    }
}
