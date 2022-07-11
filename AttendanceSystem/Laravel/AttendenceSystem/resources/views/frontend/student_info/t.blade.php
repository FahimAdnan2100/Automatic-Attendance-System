@extends('frontend.user_master')
@section('frontend')

	  <div class="container-full">
		<!-- Content Header (Page header) -->


		<!-- Main content -->
		<section class="content">
		  <div class="row">


            <div class="col-8">
			 <div class="box">
				<div class="box-header with-border">
				  <h3 class="box-title">Teacher List</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body " style="text-align: center;">
					@for ($i=1 ;$i<31; $i++)


				<div class="col-xl-3 col-6">
					<div class="box overflow-hidden pull-up">
						<div class="box-body"  >

							<div class="icon bg-primary-light rounded w-60 h-60">
								<i class="text-primary mr-0 font-size-24 mdi mdi-account-multiple"></i>
							</div>
							<div>
                                <a class="text-mute mt-20 mb-0 font-size-16" href="{{route('info.course',[$i,$depts])}}">Batch: {{$i}} </a>


							</div>
						</div>
					</div>
				</div>


                @endfor
				</div>
				<!-- /.box-body -->
			  </div>
			  <!-- /.box -->


			  <!-- /.box -->

            </div>
			<!-- /.col -->

            <!-- ----------------Add Brand-------------- -->

            <div class="col-4">
                <div class="box">
                   <div class="box-header with-border">
                     <h3 class="box-title">Add Department</h3>
                   </div>
                   <!-- /.box-header -->
                   <div class="box-body">
                       <div class="table-responsive">


                           <form method="POST" action="{{ route('s_info.store') }}" enctype="multipart/form-data">
                               @csrf

                                           <div class="form-group">
                                           <h5>Enter Teacher Name <span class="text-danger">*</span></h5>
                                           <div class="controls">
                                               <input type="text" name="name"  class="form-control"  >
                                           @error('name')
                                               <span class="text-danger">{{$message}}</span>
                                           @enderror
                                           </div>
                                           </div>
                                           <div class="form-group">
                                               <h5>Enter Student ID <span class="text-danger">*</span></h5>
                                               <div class="controls">
                                                   <input type="text" name="s_id"  class="form-control"  >
                                               @error('s_id')
                                                   <span class="text-danger">{{$message}}</span>
                                               @enderror
                                               </div>
                                               </div>






                                   <div class="text-xs-right">
                                       <input type="submit" class="btn btn-rounded btn-primary mb-5" value="Add Info" >
                                   </div>
                               </form>

                       </div>
                   </div>
                   <!-- /.box-body -->
                 </div>
                 <!-- /.box -->


                 <!-- /.box -->

               </div>
			<!-- /.col -->



		  </div>
		  <!-- /.row -->
		</section>
		<!-- /.content -->

	  </div>




@endsection
