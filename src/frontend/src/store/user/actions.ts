import { createAsyncThunk } from '@reduxjs/toolkit'
import { userAPI } from '../../api/user'

export const fetchUser = createAsyncThunk('user/fetchUser', async () => {
	return await userAPI.getUser()
})
