@php
    $prefix = Request::route()->getPrefix();
    $route = Route::current()->getName();
@endphp
<aside class="main-sidebar">
    <!-- sidebar-->
    <section class="sidebar">

        <div class="user-profile">
			<div class="ulogo">
				 <a href="{{url('dashboard')}}">
				  <!-- logo for regular state and mobile devices -->
					 <div class="d-flex align-items-center justify-content-center">
                     <img style="height: 20px;width:20px" src="{{asset('frontend/images/avatar/33.png')}}" alt="">
						  <h3><b>Admin</b> Dashboard</h3>
					 </div>
				</a>
			</div>
        </div>

      <!-- sidebar menu-->
      <ul class="sidebar-menu" data-widget="tree">

		<li class="{{ ($route=='dashboard')? 'active':'' }}">
          <a href="{{url('dashboard')}}">
            <i data-feather="pie-chart"></i>
			<span>Homepage</span>
          </a>
        </li>



        <li class="treeview {{($prefix=='/brand')? 'active':''}}">
          <a href="#">
            <i data-feather="file-plus"></i>
            <span>Add Information</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-right pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li class="{{($route=='all.dept')? 'active':''}}"><a href="{{route('all.dept')}}"><i class="ti-more"></i>Add Dept</a></li>
            <li class="{{($route=='all.info')? 'active':''}}"><a href="{{route('all.info')}}"><i class="ti-more"></i>Teacher Info</a></li>
            <li class="{{($route=='all.s_info')? 'active':''}}"><a href="{{route('all.s_info')}}"><i class="ti-more"></i>Student Info</a></li>
            <li class="{{($route=='all.course')? 'active':''}}"><a href="{{route('all.course')}}"><i class="ti-more"></i>Add Course</a></li>
        </ul>
        </li>


        {{-- <li class="header nav-small-cap">User Interface</li> --}}







      </ul>
    </section>

	<div class="sidebar-footer">
		<!-- item-->
		<a href="javascript:void(0)" class="link" data-toggle="tooltip" title="" data-original-title="Settings" aria-describedby="tooltip92529"><i class="ti-settings"></i></a>
		<!-- item-->
		<a href="mailbox_inbox.html" class="link" data-toggle="tooltip" title="" data-original-title="Email"><i class="ti-email"></i></a>
		<!-- item-->
		<a href="{{ route('user.logout') }}" class="link" data-toggle="tooltip" title="" data-original-title="Logout"><i class="ti-lock"></i></a>
	</div>
  </aside>
