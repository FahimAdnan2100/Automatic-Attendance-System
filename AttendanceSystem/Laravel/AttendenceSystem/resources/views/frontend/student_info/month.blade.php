@extends('frontend.user_master')
@section('frontend')


<div class="container-full">

		<!-- Main content -->
		<section class="content">
			<div class="row">
                @for ($i=1 ;$i<13; $i++)


				<div class="col-xl-3 col-6">
					<div class="box overflow-hidden pull-up">
						<div class="box-body"  >

							<div class="icon bg-primary-light rounded w-60 h-60">
								<i class="text-primary mr-0 font-size-24 mdi mdi-account-multiple"></i>
							</div>
							<div>
                                <a class="text-mute mt-20 mb-0 font-size-16" href="{{route('info.day',[$i,$year,$course_no,$batch,$dept])}}">Month: {{$i}} </a>


							</div>
						</div>
					</div>
				</div>


                @endfor



			</div>
		</section>
		<!-- /.content -->
	  </div>
@endsection
