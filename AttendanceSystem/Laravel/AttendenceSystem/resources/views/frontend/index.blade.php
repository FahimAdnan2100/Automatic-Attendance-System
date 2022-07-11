@extends('frontend.user_master')
@section('frontend')


<div class="container-full">
@php
    $depts = App\Models\Dept::orderBy('dept','ASC')->get();
    $totals = App\Models\StudentInfo::latest()->get();
    $count=0;
@endphp
		<!-- Main content -->
		<section class="content">
			<div class="row">
                @foreach ($depts as $dept)

                    @foreach ($totals as $total)
                        @php

                            if($dept->id==$total->dept_id){
                                $count=$count+1;
                            }
                        @endphp
@endforeach
				<div class="col-xl-3 col-6">
					<div class="box overflow-hidden pull-up">
						<div class="box-body"  >

							<div class="icon bg-primary-light rounded w-60 h-60">
								<i class="text-primary mr-0 font-size-24 mdi mdi-account-multiple"></i>
							</div>
							<div>
                                <a class="text-mute mt-20 mb-0 font-size-16" href="{{route('info.batch',$dept->id)}}">{{$dept->dept}} </a>
								
								<p class="text-mute mt-20 mb-0 font-size-16">Total Student: {{$count}}</p>
							</div>
						</div>
					</div>
				</div>
                        @php
                        $count=0;
                        @endphp

                @endforeach



			</div>
		</section>
		<!-- /.content -->
	  </div>
@endsection
