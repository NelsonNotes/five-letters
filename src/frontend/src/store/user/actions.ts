import { createAsyncThunk } from '@reduxjs/toolkit'
import { userAPI } from '../../api/user'

export const fetch = createAsyncThunk('user/fetchUser', async () => {
	return await userAPI.getUser()
})
