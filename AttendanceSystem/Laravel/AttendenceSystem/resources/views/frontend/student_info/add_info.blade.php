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
					<div class="table-responsive">
					  <table id="example1" class="table table-bordered table-striped">
						<thead>
							<tr>
                                <th>Teacher Name</th>
								<th>Department</th>
                                <th>Image</th>
								<th>Action</th>

							</tr>
						</thead>
						<tbody>
                            @foreach ($infos as $item)


							<tr>
                                <td>{{$item->name}}</td>
								<td>{{$item['depts']['dept']}}</td>
                                <td>
                                    <img src="{{asset($item->teacher_photo_path)}}" style="width:40px;height:40px" alt="">
                                </td>
								<td>
                                    <a href="#" class="btn btn-info">Edit</a>
                                    <a href="#" class="btn btn-danger" id="delete">Delete</a>
                                </td>
                                {{-- {{ route('info.edit',$item->id) }}
                                {{ route('info.delete',$item->id) }} --}}
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
				  <h3 class="box-title">Add Information</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body">
					<div class="table-responsive">


                    <form method="POST" action="{{ route('info.store') }}" enctype="multipart/form-data">
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
                                    <h5>Select Department <span class="text-danger">*</span></h5>
                                    <div class="controls">
                                        <select name="dept_id" class="form-control"  >
                                            <option value="" selected="" disabled="">Select Department</option>
                                            @foreach($depts as $dept)
                                            <option value="{{ $dept->id }}">{{ $dept->dept }}</option>
                                            @endforeach
                                        </select>
                                        @error('dept_id')
                                     <span class="text-danger">{{ $message }}</span>
                                     @enderror
                                     </div>
                                    </div>

                                    <div class="form-group">
                                        <h5>Teacher Image <span class="text-danger">*</span></h5>
                                        <div class="controls">
                                            <input type="file" name="teacher_photo_path"  class="form-control"  >
                                            @error('teacher_photo_path')
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
