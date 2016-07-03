var app = angular.module('myToDoList', [
		'ui.router'
	]);

app.constant('BASE_URL', 'http://localhost:8000/api/tasks/');

app.config(function($stateProvider, $urlRouterProvider){
	$stateProvider
		.state('index', {
			url: '/',
			templateUrl: '/static/templates/index.html',
			controller: 'MainCtrl'
		})
		.state('add-task', {
			url: '/add',
			templateUrl: 'static/templates/add.html',
			controller: 'MainCtrl'
		});

	$urlRouterProvider.otherwise('/');
});

app.service('Tasks', function($http, BASE_URL){
	var Tasks = {};

	this.all = function(){
		return $http.get(BASE_URL);
	};

	this.update = function(updatedTask){
		return $http.put(BASE_URL + updatedTask.id + '/', updatedTask);
	};

	this.delete = function(id){
		return $http.delete(BASE_URL + id + '/');
	};

	this.addOne = function(newTask){
		return $http.post(BASE_URL, newTask)
	};
});

app.controller('MainCtrl', function($scope, Tasks, $state){

	$scope.newTask = {};

	$scope.addTask = function(){
		Tasks.addOne($scope.newTask)
			.then(function(res){
				$state.go('index');
			});
	};

	$scope.toggleCompleted = function(task){
		Tasks.update(task);
	};

	$scope.deleteTask = function(id){
		Tasks.delete(id);
		$scope.tasks = $scope.tasks.filter(function(task){
			return task.id !== id;
		})
	};

	Tasks.all().then(function(res){
		$scope.tasks = res.data;
	});

});