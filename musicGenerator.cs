using System;
using System.IO;
using CsvHelper;
using System.Collections.Generic;

namespace MusicGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            ReadDirectories musicDirectory = new ReadDirectories(@"H:\Music");
            CsvClass csv = new CsvClass();
            csv.CsvWriter(musicDirectory.bandAlbums);
        }
    }

    class ReadDirectories
    {
        public Dictionary<string, AlbumDisco> bandAlbums = new Dictionary<string, AlbumDisco>();
        public ReadDirectories(string path)
        {
            string[] directories = Directory.GetDirectories(path);

            foreach (var band in directories)
            {
                // Read last part of array instead of selecting the position
                string bandName = band.Split("\\")[band.Split("\\").Length - 1];
                bandAlbums.Add(bandName, new AlbumDisco());
                string[] albumPath = Directory.GetDirectories(band);

                foreach (var album in albumPath)
                {
                    // Read last part of array instead of selecting the position
                    string albumName = album.Split("\\")[album.Split("\\").Length - 1];
                    bandAlbums[bandName].discography.Add(albumName, new List<string>());
                    string[] songPath = Directory.GetFiles(album);

                    foreach(var songs in songPath)
                    {
                        // Read last part of array instead of selecting the position
                        string song = songs.Split("\\")[songs.Split("\\").Length - 1];
                        bandAlbums[bandName].discography[albumName].Add(song);
                    }
                }
            }
        }
    }

    class AlbumDisco
    {
        // Object to contain album and songs
        public Dictionary<string, List<string>> discography = new Dictionary<string, List<string>>();
    }

    class CsvClass
    {
        public void CsvWriter(Dictionary<string, AlbumDisco> data)
        {
            using (var w = new StreamWriter(@"C:\MusicGenerator\music.csv"))
            using (var csv = new CsvWriter(w))
            {
                foreach (var b in data.Keys)
                {
                    foreach (var a in data[b].discography.Keys)
                    {
                        foreach (var s in data[b].discography[a])
                        {
                            csv.WriteField(b);
                            csv.WriteField(a);
                            csv.WriteField(s);
                            csv.NextRecord();
                        }
                    }
                }
            }
        }
    }
}
