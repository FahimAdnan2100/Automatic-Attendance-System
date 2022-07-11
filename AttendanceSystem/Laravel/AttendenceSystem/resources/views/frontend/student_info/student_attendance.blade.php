@extends('frontend.user_master')
@section('frontend')

	  <div class="container-full">
		<!-- Content Header (Page header) -->


		<!-- Main content -->
		<section class="content">
		  <div class="row">


            <div class="col-12">
			 <div class="box">
				<div class="box-header with-border">
				  <h3 class="box-title">Student Attendance List</h3>
				</div>
				<!-- /.box-header -->
				<div class="box-body " style="text-align: center;">
					<div class="table-responsive">
					  <table id="example1" class="table table-bordered table-striped">
						<thead>
							<tr>
                                <th>Name</th>
                                <th>ID</th>
                                <th>Dept</th>
                                <th>batch</th>
                                <th>Course_no</th>
                                <th>Year</th>
                                <th>Month</th>
                                <th>Date</th>
                                <th>Time</th>
                            


								<th>Action</th>

							</tr>
						</thead>
						<tbody>
                            @foreach ($attendances as $item)


							<tr>
                                <td>{{$item->name}}</td>
                                <td>{{$item->s_id}}</td>
								<td>{{$item->dept}}</td>
                                <td>{{$item->batch}}</td>
                                <td>{{$item->course_no}}</td>
                                <td>{{$item->year}}</td>
                                <td>{{$item->month}}</td>
                                <td>{{$item->date}}</td>
                                <td>{{$item->time}}</td>
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


			<!-- /.col -->



		  </div>
		  <!-- /.row -->
		</section>
		<!-- /.content -->

	  </div>




@endsection
