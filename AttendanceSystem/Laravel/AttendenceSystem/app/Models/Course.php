<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Course extends Model
{
    use HasFactory;
    protected $fillable = [
        'dept_id',
        'batch',
        'course_no',
        'course_name'
    ];
    public function depts(){
        return $this->belongsTo(Dept::class,'dept_id','id');
    }
}
