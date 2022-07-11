<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class StudentInfo extends Model
{
    use HasFactory;
    protected $fillable = [
        'name',
        's_id',
        'dept_id',
        'batch',
        'email',
        'phone'

    ];
    public function depts(){
        return $this->belongsTo(Dept::class,'dept_id','id');
    }
}
