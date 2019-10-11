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
        public Dictionary<string, Dictionary<string, List<string>>> bandAlbums = new Dictionary<string, Dictionary<string, List<string>>>();
        public ReadDirectories(string path)
        {
            string[] directories = Directory.GetDirectories(path);

            foreach (var band in directories)
            {
                // Read last part of array instead of selecting the position
                string bandName = band.Split("\\")[2];
                bandAlbums.Add(bandName, new Dictionary<string, List<string>>());
                string[] albumPath = Directory.GetDirectories(band);

                foreach (var album in albumPath)
                {
                    // Read last part of array instead of selecting the position
                    string albumName = album.Split("\\")[3];
                    bandAlbums[bandName].Add(albumName, new List<string>());
                    string[] songPath = Directory.GetFiles(album);

                    foreach(var songs in songPath)
                    {
                        // Read last part of array instead of selecting the position
                        string song = songs.Split("\\")[4];
                        bandAlbums[bandName][albumName].Add(song);
                    }
                }
            }
        }
    }

    class CsvClass
    {
        public void CsvWriter(Dictionary<string, Dictionary<string, List<string>>> data)
        {
            using (var w = new StreamWriter(@"C:\MusicGenerator\music.csv"))
            using (var csv = new CsvWriter(w))
            {
                foreach (var b in data.Keys)
                {
                    foreach (var a in data[b].Keys)
                    {
                        foreach (var s in data[b][a])
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
