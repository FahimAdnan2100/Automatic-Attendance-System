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
				  <h3 class="box-title">Department List</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body " style="text-align: center;">
					<div class="table-responsive">
					  <table id="example1" class="table table-bordered table-striped">
						<thead>
							<tr>

								<th>Department Name</th>
								<th>Action</th>

							</tr>
						</thead>
						<tbody>
                            @foreach ($depts as $item)


							<tr>
								<td>{{$item->dept}}</td>

								<td>
                                    <a href="{{ route('dept.edit',$item->id) }}" class="btn btn-info">Edit</a>
                                    <a href="{{ route('dept.delete',$item->id) }}" class="btn btn-danger" id="delete">Delete</a>
                                </td>

							</tr>
                            @endforeach
						</tbody>

					  </table>
					</div>
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


                    <form method="POST" action="{{ route('dept.store') }}" enctype="multipart/form-data">
                    @csrf

                                <div class="form-group">
								<h5>Enter Department Name <span class="text-danger">*</span></h5>
								<div class="controls">
									<input type="text" name="dept"  class="form-control"  >
                                @error('dept')
                                    <span class="text-danger">{{$message}}</span>
                                @enderror
                                </div>
							    </div>


						<div class="text-xs-right">
							<input type="submit" class="btn btn-rounded btn-primary mb-5" value="Add Dept" >
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
