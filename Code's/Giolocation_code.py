

   # Page Code End---------------------------------------------------
# <!-- <!-- ---------for address--------------------- -->
						<fieldset>
							<div class="form-group">
							<label for="map">Address<span style="color:red">*</span> :</label>
							<div class="row">
							<div class="col-md-12">
							<div class="input-group no-margin">
							<input type="text" id="sup_search_loc" class="MAP_LOCATION form-control">
							<div class="input-group-btn">
							<a href="javascript:;" id="search_loc" class="btn btn-xs btn-default no-margin" >
							<i class="fa fa-search" style="font-size:28px;"></i>
							</a>
							
							</div>
							</div>
							</div>
							<div class="col-md-12">
							<div id="mapdiv" style="width: 99.7%; height: 200px;">

							</div>
							</div>
							</div>
							<span id="error_driveraddress" style="display:none;color:red;">Please Enter Driver Address.</span>
							</div>
							<div class="row hide">
							<div class="col-md-6">
							<div class="form-group">
							<label for="sup_latitude" class="control-label">Latitude</label>
							<div class="input-group">
							<input class="form-control" id="latitude" name="sup_latitude" type="text">
							<div class="input-group-btn">
							<a href="javascript:;" class="LAT_LNG_MAP btn btn-xs btn-default no-margin">
							<i class="fa fa-search"></i>
							</a>
							</div>
							</div>
							</div>
							</div>
							<div class="col-md-6">
							<div class="form-group">
							<label for="sup_longitude" class="control-label">Longitude</label>
							<div class="input-group">
							<input class="form-control" id="longitude" name="sup_longitude" type="text">
							<div class="input-group-btn">
							<a href="javascript:;" class="LAT_LNG_MAP btn btn-xs btn-default no-margin">
							<i class="fa fa-search"></i>
							</a>
							</div>
							</div>
							</div>
							</div>
							</div>
						</fieldset>
						
						<script>
							<!-- <!-- <!-- <!-- for address map --> --> --> -->
							 $(document).ready(function () {
								var MAPDIV = new google.maps.Map(document.getElementById('mapdiv'), {
									<!-- center: new google.maps.LatLng('51.498', '-0.126'), -->
									center: new google.maps.LatLng('40.4453502', '-3.6863012'),
									zoom: 8,
									mapTypeId: google.maps.MapTypeId.ROADMAP,
									streetViewControl: false
								});
								var MAPDIV_MARKER = new google.maps.Marker({
									<!-- position: new google.maps.LatLng('51.498', '-0.126'), -->
									position: new google.maps.LatLng('40.4453502', '-3.6863012'),
									map: MAPDIV,
									draggable: true
								});
								google.maps.event.addListener(MAPDIV_MARKER, 'dragend', function () {
									MAP_LAT_LNG();
								});

								var MAP_GEOCODER = new google.maps.Geocoder();

								var MAP_LAT_LNG = function () {
									var LAT_LNG = MAPDIV_MARKER.getPosition();
									MAPDIV.panTo(LAT_LNG);
									$('input[name="sup_latitude"]').val(LAT_LNG.lat());
									$('input[name="sup_longitude"]').val(LAT_LNG.lng());

									MAP_GEOCODER.geocode({
										latLng: LAT_LNG
									}, function (results, status) {
										if (status == google.maps.GeocoderStatus.OK) {
											$('.MAP_LOCATION').val(results[0].formatted_address);
										}
									});
								};
								var LAT_LNG_MAP = function () {
									var LAT = $('input[name="sup_latitude"]').val().trim();
									var LNG = $('input[name="sup_longitude"]').val().trim();
									if ($.isNumeric(LAT) && $.isNumeric(LNG) && (-90 <= LAT) && (LAT <= 90) && (-180 <= LNG) && (LNG <= 180)) {
										var LAT_LNG = new google.maps.LatLng(LAT, LNG);
										MAPDIV.setCenter(LAT_LNG);
										MAPDIV_MARKER.setPosition(LAT_LNG);

										if (!$('.MAP_LOCATION').val()) {
											MAP_GEOCODER.geocode({
												latLng: LAT_LNG
											}, function (results, status) {
												if (status == google.maps.GeocoderStatus.OK) {
													$('.MAP_LOCATION').val(results[0].formatted_address);
												}
											});
										}
									} else {
										window.alert('Latitude and Longitude is error');
									}
								};
								$('.LAT_LNG_MAP').on('click', function () {
									LAT_LNG_MAP();
								});
								if ($('input[name="sup_latitude"]').val().trim() && $('input[name="sup_longitude"]').val().trim()) {
									$('.LAT_LNG_MAP').trigger('click');
								}

								$('#search_loc').click(function () {
									var address = $('.MAP_LOCATION').val();
									MAP_GEOCODER.geocode({'address': address}, function (results, status) {
										if (status == google.maps.GeocoderStatus.OK) {
											MAPDIV.setCenter(results[0].geometry.location);
											MAPDIV_MARKER.setPosition(results[0].geometry.location);
											$('input[name="sup_latitude"]').val(results[0].geometry.location.lat());
											$('input[name="sup_longitude"]').val(results[0].geometry.location.lng());
										} else {
											alert("Location was not successful for the following reason: " + status);
										}
									});
								});

								var MAP_AUTOCOMPLETE = new google.maps.places.Autocomplete($('.MAP_LOCATION')[0], {
									componentRestrictions: {
										country: 'ES'
									}
								});
								MAP_AUTOCOMPLETE.addListener('place_changed', function () {
									var place = MAP_AUTOCOMPLETE.getPlace();
									if (!place || !place.geometry) {
										console.log("Autocomplete's returned place contains no geometry");
										return;
									}

									MAPDIV.setCenter(place.geometry.location);
									MAPDIV_MARKER.setPosition(place.geometry.location);

									$('input[name="sup_latitude"]').val(place.geometry.location.lat());
									$('input[name="sup_longitude"]').val(place.geometry.location.lng());
								});

								$('.MAP_LOCATION').on('keydown', function (ev) {
									if (ev.keyCode === 13) {
										ev.preventDefault();
										$('#search_loc').trigger('click');
									}
								});
							});
						
						</script>
                        
                        
                        
                        # Page Code End---------------------------------------------------
                        
                        Add Script with google api key
                        # <!-- geolocation script for address -->
  <script data-cfasync='false' type='text/javascript' src='https://maps.googleapis.com/maps/api/js?libraries=geometry,places&key=AIzaSyCGMBLupqHbszOe6a_KWwdhFAZmZKFT2gU'></script>
  # <!-- geolocation script for address -->
                        
                        
                        