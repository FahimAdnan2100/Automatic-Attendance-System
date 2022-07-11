@extends('frontend.user_master')
@section('frontend')


<div class="container-full">
		<!-- Content Header (Page header) -->


		<!-- Main content -->
		<section class="content">
		  <div class="row">



			<!-- /.col -->

            <!-- ----------------Add Brand-------------- -->

            <div class="col-12">
			 <div class="box">
				<div class="box-header with-border">
				  <h3 class="box-title">Add Information</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body">
					<div class="table-responsive">


                    <form method="POST" action="{{ route('info.store') }}" enctype="multipart/form-data">
                    @csrf

                                <div class="form-group">
								<h5>Student Name <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="name"  class="form-control"  >
                                @error('name')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>

                                <div class="form-group">
								<h5>Student ID <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="sid"  class="form-control"  >
                                    @error('sid')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>
                                <div class="form-group">
								<h5>Department <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="dept"  class="form-control"  >
                                    @error('dept')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>
                                <div class="form-group">
								<h5>Batch NO <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="batch"  class="form-control"  >
                                    @error('batch')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>
                                <div class="form-group">
								<h5>Email <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="email"  class="form-control"  >
                                    @error('email')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>
                                <div class="form-group">
								<h5>Phone Number<span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="phone"  class="form-control"  >
                                    @error('phone')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>

                                <div class="form-group">
								<h5>Student Image <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="file" name="student_photo_path"  class="form-control"  >
                                    @error('student_photo_path')
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
