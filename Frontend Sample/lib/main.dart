import 'dart:async';
import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Underground Discovery',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final PageController _pageController = PageController();
  int _currentPage = 0;
  bool _isScrollDisabled = false;

  @override
  void initState() {
    super.initState();
    _pageController.addListener(() {
      int nextPage = _pageController.page?.round() ?? 0;
      if (_currentPage != nextPage) {
        setState(() {
          _currentPage = nextPage;
        });

        if (nextPage == 2) {
          setState(() {
            _isScrollDisabled = true;
          });
          Timer(Duration(seconds: 10), () {
            setState(() {
              _isScrollDisabled = false;
            });
          });
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          NotificationListener<ScrollNotification>(
            onNotification: (scrollNotification) =>
                _isScrollDisabled ? true : false,
            child: PageView(
              controller: _pageController,
              scrollDirection: Axis.vertical,
              children: [
                VideoPage(videoAsset: 'assets/video_10.mp4'),
                VideoPage(videoAsset: 'assets/video_9.mp4'),
                VideoPage(videoAsset: 'assets/video_11.mp4'),
                VideoPage(videoAsset: 'assets/video_7.mp4'),
                VideoPage(videoAsset: 'assets/video_8.mp4'),
                // Add more VideoPage instances as needed
              ],
            ),
          ),
          if (_currentPage == 2)
            Positioned(
              bottom: 80,
              left: 20,
              right: 20,
              child: Center(
                child: Container(
                  padding: EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.7),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: GestureDetector(
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => SecondPage(
                              highlightedSong: 'Free (with Drew Love)'),
                        ),
                      );
                    },
                    child: Text(
                      "Recommended Song -> Free (with Drew Love)",
                      style: TextStyle(
                        fontSize: 16,
                        color: Colors.black,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          Positioned(
            bottom: 20,
            left: 0,
            right: 0,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                IconButton(
                  icon: Icon(Icons.home, color: Colors.white),
                  onPressed: () {
                    Navigator.pushAndRemoveUntil(
                      context,
                      MaterialPageRoute(builder: (context) => HomePage()),
                      (Route<dynamic> route) => false,
                    );
                  },
                ),
                IconButton(
                  icon: Icon(Icons.search, color: Colors.white),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              SecondPage(highlightedSong: '')),
                    );
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class VideoPage extends StatefulWidget {
  final String videoAsset;

  VideoPage({required this.videoAsset});

  @override
  _VideoPageState createState() => _VideoPageState();
}

class _VideoPageState extends State<VideoPage> {
  late VideoPlayerController _controller;
  late Future<void> _initializeVideoPlayerFuture;

  @override
  void initState() {
    super.initState();
    _controller = VideoPlayerController.asset(widget.videoAsset);
    _initializeVideoPlayerFuture = _controller.initialize();
    _controller.setLooping(true);
    _controller.play();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: _initializeVideoPlayerFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          return Center(
            child: AspectRatio(
              aspectRatio: _controller.value.aspectRatio,
              child: VideoPlayer(_controller),
            ),
          );
        } else {
          return Center(child: CircularProgressIndicator());
        }
      },
    );
  }
}

class SecondPage extends StatefulWidget {
  final String highlightedSong;

  SecondPage({required this.highlightedSong});

  @override
  _SecondPageState createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  final List<Song> songs = [
    Song("Free (with Drew Love)", "Louis The Child, Drew Love"),
    Song("Fire", "Louis The Child, Evalyn"),
    Song("Love is Alive", "Louis The Child, Elohim"),
    Song("Bedroom", "Litany"),
    Song("Falling (with NJOMZA & Daniel Allan)",
        "Louis The Child, NJOMZA, Daniel Allan"),
    Song("Pierre", "Ryn Weaver"),
    Song("What's It Gonna Be?", "Shura"),
    Song("Touch", "Shura"),
    Song("Call On Me", "Litany"),
    Song("My Dude", "Litany"),
    Song("religion (u can lay your hands on me)", "Shura"),
    Song("Stay With Me (with Absolutely)", "Louis The Child, Absolutely"),
    Song("Cool Kids - Sped Up",
        "Echosmith, Sped Up Songs + Nightcore, Nightcore"),
    Song("Adult Movies", "Litany"),
    Song("Playlist", "Litany, Oscar Scheller"),
    Song("Home Is You", "ROZES"),
    Song("Capsize - Dzeko & Torres", "FRENSHIP, Emily Warren, Dzeko & Torres"),
    Song("Make It Up", "Shura"),
    Song(
        "Electric Touch - Midnight Kids Remix", "A R I Z O N A, Midnight Kids"),
    Song("Sensations (Whethan Remix)", "Elohim, Whethan")
  ];

  bool _isHighlighted = false;
  Timer? _timer;

  @override
  void initState() {
    super.initState();
    if (widget.highlightedSong.isNotEmpty) {
      _startBlinking();
    }
  }

  void _startBlinking() {
    _isHighlighted = true;
    _timer = Timer.periodic(Duration(milliseconds: 500), (timer) {
      setState(() {
        _isHighlighted = !_isHighlighted;
      });
    });

    Timer(Duration(seconds: 5), () {
      _timer?.cancel();
      setState(() {
        _isHighlighted = false;
      });
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Underground Discovery'),
      ),
      body: ListView.builder(
        itemCount: songs.length,
        itemBuilder: (context, index) {
          final song = songs[index];
          return Container(
            color: song.title == widget.highlightedSong && _isHighlighted
                ? Colors.yellow
                : null,
            child: ListTile(
              title: Text(song.title),
              subtitle: Text(song.artist),
            ),
          );
        },
      ),
    );
  }
}

class Song {
  final String title;
  final String artist;

  Song(this.title, this.artist);
}
