<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class StudentAttendance extends Model
{
    use HasFactory;
    protected $fillable = [
        'name',
        's_id',
        'dept',
        'batch',
        'course_no',
        'year',
        'month',
        'date',
        'time',
        'status'
    ];
}
