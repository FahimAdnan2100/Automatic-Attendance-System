<?php

use App\Http\Controllers\AdminController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Backend\AdminProfileController;
use App\Http\Controllers\Frontend\IndexController;
use App\Http\Controllers\Frontend\DeptController;
use App\Http\Controllers\Frontend\TeacherInfoController;
use App\Http\Controllers\Frontend\StudentInfoController;
use App\Http\Controllers\Frontend\CourseController;
use App\Http\Controllers\Frontend\InfoController;
use Illuminate\Support\Facades\Auth;
use App\Models\User;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});


Route::group(['prefix'=> 'admin','middleware'=>['admin:admin']],function(){
    Route::get('/login',[AdminController::class,'loginForm']);
    Route::post('/login',[AdminController::class,'store'])->name('admin.login');
    Route::get('/register',[AdminController::class,'registerFrom']);
    Route::post('/register',[AdminController::class,'storeFrom'])->name('admin.register');
});


Route::middleware(['auth:sanctum,admin', 'verified'])->get('/admin/dashboard', function () {


    return view('admin.index');
})->name('dashboard');

Route::middleware(['auth:sanctum,web', 'verified'])->get('/dashboard', function () {
    $id = Auth::user()->id;
    $editData = User::find($id);
    return view('frontend.index',compact('editData'));
})->name('dashboard');
//Admin alll route
Route::get('/admin/logout',[AdminController::class,'destroy'])->name('admin.logout');
Route::get('/admin/profile',[AdminProfileController::class,'AdminProfile'])->name('admin.profile');
Route::get('/admin/profile/edit',[AdminProfileController::class,'AdminProfileEdit'])->name('admin.profile.edit');
Route::post('/admin/profile/store',[AdminProfileController::class,'AdminProfileStore'])->name('admin.profile.store');
Route::get('/admin/change/password',[AdminProfileController::class,'AdminChangePassword'])->name('admin.change.password');
Route::post('/update/change/password',[AdminProfileController::class,'UpdateChangePassword'])->name('admin.update.password');

Route::get('/',[IndexController::class,'index']);
Route::get('/user/logout',[IndexController::class,'UserLogout'])->name('user.logout');
Route::get('/user/profile/edit',[IndexController::class,'UserProfileEdit'])->name('user.profile.edit');
Route::get('/user/profile',[IndexController::class,'UserProfileUpdate'])->name('user.profile');
Route::post('/user/profile/store',[IndexController::class,'UserProfileStore'])->name('user.profile.store');



//Add Department
Route::prefix('dept')->group(function(){
    Route::get('/view',[DeptController::class,'DeptView'])->name('all.dept');
    Route::post('/store',[DeptController::class,'DeptStore'])->name('dept.store');
    Route::get('/edit/{id}',[DeptController::class,'DeptEdit'])->name('dept.edit');
    Route::post('/update',[DeptController::class,'DeptUpdate'])->name('dept.update');
    Route::get('/delete/{id}',[DeptController::class,'DeptDelete'])->name('dept.delete');
});

Route::prefix('info')->group(function(){
    Route::get('/view',[TeacherInfoController::class,'InfoView'])->name('all.info');
    Route::post('/store',[TeacherInfoController::class,'InfoStore'])->name('info.store');
    Route::get('/edit/{id}',[TeacherInfoController::class,'InfoEdit'])->name('info.edit');
    Route::post('/update',[TeacherInfoController::class,'InfoUpdate'])->name('info.update');
    Route::get('/delete/{id}',[TeacherInfoController::class,'InfoDelete'])->name('info.delete');
});



//add student info
Route::prefix('s_info')->group(function(){
    Route::get('/view',[StudentInfoController::class,'InfoView'])->name('all.s_info');
    Route::post('/store',[StudentInfoController::class,'InfoStore'])->name('s_info.store');
    Route::get('/edit/{id}',[StudentInfoController::class,'InfoEdit'])->name('s_info.edit');
    Route::post('/update',[StudentInfoController::class,'InfoUpdate'])->name('s_info.update');
    Route::get('/delete/{id}',[StudentInfoController::class,'InfoDelete'])->name('s_info.delete');
});

Route::prefix('course')->group(function(){
    Route::get('/view',[CourseController::class,'InfoView'])->name('all.course');
    Route::post('/store',[CourseController::class,'InfoStore'])->name('course.store');
    Route::get('/edit/{id}',[CourseController::class,'InfoEdit'])->name('course.edit');
    Route::post('/update',[CourseController::class,'InfoUpdate'])->name('course.update');
    Route::get('/delete/{id}',[CourseController::class,'InfoDelete'])->name('course.delete');
});
Route::prefix('info')->group(function(){
    Route::get('batch/{id}',[InfoController::class,'BatchView'])->name('info.batch');
    Route::get('course/{id}/{id1}',[InfoController::class,'CourseView'])->name('info.course');
    Route::get('year/{id}/{id1}/{id2}',[InfoController::class,'InfoYear'])->name('info.year');
    Route::get('month/{id}/{id1}/{id2}/{id3}',[InfoController::class,'InfoMonth'])->name('info.month');
    Route::get('day/{id}/{id1}/{id2}/{id3}/{id4}',[InfoController::class,'InfoDay'])->name('info.day');
    Route::get('attendance/{id}/{id1}/{id2}/{id3}/{id4}/{id5}',[InfoController::class,'AttendanceInfo'])->name('info.attendance');
});

//Admin Category All Routes


