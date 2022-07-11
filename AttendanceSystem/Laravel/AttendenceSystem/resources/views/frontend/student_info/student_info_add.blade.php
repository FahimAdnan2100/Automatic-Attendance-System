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
				  <h3 class="box-title">Student List</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body " style="text-align: center;">
					<div class="table-responsive">
					  <table id="example1" class="table table-bordered table-striped">
						<thead>
							<tr>
                                <th>Name</th>
                                <th>ID</th>
								<th>Department</th>
                                <th>Batch</th>
                                <th>Image</th>
								<th>Action</th>

							</tr>
						</thead>
						<tbody>
                            @foreach ($infos as $item)


							<tr>
                                <td>{{$item->name}}</td>
                                <td>{{$item->s_id}}</td>
								<td>{{$item['depts']['dept']}}</td>
                                <td>{{$item->batch}}</td>
                                <td>
                                    <img src="{{asset($item->student_photo_path)}}" style="width:40px;height:40px" alt="">
                                </td>
								<td>
                                    <a href="#" class="btn btn-info"><i class="fa fa-pencil"></i></a>
                                    <a href="#" class="btn btn-danger"><i class="fa fa-trash"></i></a>
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
				  <h3 class="box-title">Add Student Information</h3>
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
                                        <h5>Select Bacth No <span class="text-danger">*</span></h5>
                                        <div class="controls">
                                            <select name="batch"    class="form-control" >
                                                <option value="" selected="" disabled="">Select Batch</option>
                                                <option value="1">1</option>
                                                <option value="2">2</option>
                                                <option value="3">3</option>
                                                <option value="4">4</option>
                                                <option value="5">5</option>
                                                <option value="6">6</option>
                                                <option value="7">7</option>
                                                <option value="8">8</option>
                                                <option value="9">9</option>
                                                <option value="10">10</option>
                                                <option value="11">11</option>
                                                <option value="12">12</option>
                                                <option value="13">13</option>
                                                <option value="14">14</option>
                                                <option value="15">15</option>
                                                <option value="16">16</option>
                                                <option value="17">17</option>
                                                <option value="18">18</option>
                                                <option value="19">19</option>
                                                <option value="20">20</option>
                                                <option value="21">21</option>
                                                <option value="22">22</option>
                                                <option value="23">23</option>
                                                <option value="24">24</option>
                                                <option value="25">25</option>




                                            </select>
                                            @error('batch')
                                         <span class="text-danger">{{ $message }}</span>
                                         @enderror
                                         </div>
                                        </div>
                                        <div class="form-group">
                                            <h5>Email(baust.dept.sid@)  <span class="text-danger">*</span></h5>
                                            <div class="controls">
                                                <input type="text" name="email"  class="form-control"  >
                                            @error('email')
                                                <span class="text-danger">{{$message}}</span>
                                            @enderror
                                            </div>
                                            </div>
                                            <div class="form-group">
                                                <h5>Enter Phone Number <span class="text-danger">*</span></h5>
                                                <div class="controls">
                                                    <input type="text" name="phone"  class="form-control"  >
                                                @error('phone')
                                                    <span class="text-danger">{{$message}}</span>
                                                @enderror
                                                </div>
                                                </div>
                                    <div class="form-group">
                                        <h5>Student Image(Front Face) <span class="text-danger">*</span></h5>
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
