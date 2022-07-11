<?php

namespace App\Http\Controllers\Frontend;
use Illuminate\Contracts\Auth\StatefulGuard;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\User;
use Laravel\Fortify\Contracts\LogoutResponse;

class IndexController extends Controller
{


    public function index(){
        return view('welcome');
    }
    public function UserLogout(Request $request){
        Auth::logout();

        return Redirect()->route('login');

    }
    public function UserProfileUpdate(){
        $id = Auth::user()->id;
        $editData = User::find($id);
        return view('frontend.user_profile',compact('editData'));

    }
    public function UserProfileEdit(){
        $id = Auth::user()->id;
        $editData = User::find($id);
        return view('frontend.user_profile_edit',compact('editData'));

    }
    public function UserProfileStore(Request $request){

        $data = User::find(Auth::user()->id);
        $data->name = $request->name;
        $data->email = $request->email;


        if($request->file('profile_photo_path')){
            $file = $request->file('profile_photo_path');
            //@unlink(public_path('upload/admin_images/'.$data->profile_photo_path));
            $filename = date('YmdHi').$file->getClientOriginalName();
            $file->move(public_path('upload/user_images'),$filename);
            $data['profile_photo_path']= $filename;
        }
        $data->save();

        $notification = array(
            'message' => 'User Profile Updated Successfully',
            'alert-type' => 'success'
        );

        return redirect()->route('dashboard')->with($notification);

    }//end
}
