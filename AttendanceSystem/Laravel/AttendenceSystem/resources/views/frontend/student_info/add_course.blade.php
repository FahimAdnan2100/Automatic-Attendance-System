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
				  <h3 class="box-title">Course List</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body " style="text-align: center;">
					<div class="table-responsive">
					  <table id="example1" class="table table-bordered table-striped">
						<thead>
							<tr>
                                <th>Dept</th>
                                <th>Batch</th>
								<th>Course No</th>
                                <th>Course Name</th>
								<th>Action</th>

							</tr>
						</thead>
						<tbody>
                            @foreach ($infos as $item)


							<tr>

								<td>{{$item['depts']['dept']}}</td>
                                <td>{{$item->batch}}</td>
                                <td>{{$item->course_no}}</td>
                                <td>{{$item->course_name}}</td>
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
				  <h3 class="box-title">Add Course</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body">
					<div class="table-responsive">


                    <form method="POST" action="{{ route('course.store') }}" enctype="multipart/form-data">
                    @csrf



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
                                        <h5>Select Batch No <span class="text-danger">*</span></h5>
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
                                            <h5>Enter Course No <span class="text-danger">*</span></h5>
                                            <div class="controls">
                                                <input type="text" name="course_no"  class="form-control"  >
                                            @error('course_no')
                                                <span class="text-danger">{{$message}}</span>
                                            @enderror
                                            </div>
                                            </div>
                                            <div class="form-group">
                                                <h5>Enter Course Name <span class="text-danger">*</span></h5>
                                                <div class="controls">
                                                    <input type="text" name="course_name"  class="form-control"  >
                                                @error('course_name')
                                                    <span class="text-danger">{{$message}}</span>
                                                @enderror
                                                </div>
                                                </div>


						<div class="text-xs-right">
							<input type="submit" class="btn btn-rounded btn-primary mb-5" value="Add Course" >
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
