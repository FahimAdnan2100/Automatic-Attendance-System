<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TeacherInfo extends Model
{
    use HasFactory;
    protected $fillable = [
        'name',
        'dept_id',
    ];
    public function depts(){
        return $this->belongsTo(Dept::class,'dept_id','id');
    }
}
