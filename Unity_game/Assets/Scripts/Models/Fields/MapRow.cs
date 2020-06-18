﻿using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;

namespace Assets.Scripts.Models.Fields
{
    [Serializable]
    [SuppressMessage("ReSharper", "InconsistentNaming")]
    public class MapRow
    {
        public List<int> row = new List<int>();
    }
}
